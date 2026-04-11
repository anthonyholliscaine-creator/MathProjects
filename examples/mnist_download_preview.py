from __future__ import annotations

import gzip
import struct
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


MNIST_FILES = {
    "train_images": "train-images-idx3-ubyte.gz",
    "train_labels": "train-labels-idx1-ubyte.gz",
    "test_images": "t10k-images-idx3-ubyte.gz",
    "test_labels": "t10k-labels-idx1-ubyte.gz",
}

MNIST_BASE_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"
DATA_DIR = Path("data/mnist")
PREVIEW_PATH = Path("media/images/mnist_preview.png")


def download_file(filename: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        print(f"Using cached file: {destination}")
        return

    url = MNIST_BASE_URL + filename
    print(f"Downloading {url} -> {destination}")
    urllib.request.urlretrieve(url, destination)


def parse_images(path: Path) -> np.ndarray:
    with gzip.open(path, "rb") as handle:
        magic, count, rows, cols = struct.unpack(">IIII", handle.read(16))
        if magic != 2051:
            raise ValueError(
                f"Unexpected image magic number in {path}: {magic}")
        data = np.frombuffer(handle.read(), dtype=np.uint8)
    return data.reshape(count, rows, cols)


def parse_labels(path: Path) -> np.ndarray:
    with gzip.open(path, "rb") as handle:
        magic, count = struct.unpack(">II", handle.read(8))
        if magic != 2049:
            raise ValueError(
                f"Unexpected label magic number in {path}: {magic}")
        data = np.frombuffer(handle.read(), dtype=np.uint8)
    if len(data) != count:
        raise ValueError(
            f"Label count mismatch in {path}: expected {count}, got {len(data)}")
    return data


def load_mnist(data_dir: Path = DATA_DIR) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    paths = {key: data_dir / filename for key, filename in MNIST_FILES.items()}

    for filename in MNIST_FILES.values():
        download_file(filename, data_dir / filename)

    x_train = parse_images(paths["train_images"])
    y_train = parse_labels(paths["train_labels"])
    x_test = parse_images(paths["test_images"])
    y_test = parse_labels(paths["test_labels"])
    return x_train, y_train, x_test, y_test


def create_preview_grid(
    images: np.ndarray,
    labels: np.ndarray,
    destination: Path,
    count: int = 12,
    columns: int = 4,
    scale: int = 6,
    padding: int = 18,
) -> None:
    count = min(count, len(images))
    rows = (count + columns - 1) // columns
    digit_size = images.shape[1] * scale
    canvas_width = columns * digit_size
    canvas_height = rows * (digit_size + padding)

    canvas = Image.new("L", (canvas_width, canvas_height), color=255)
    draw = ImageDraw.Draw(canvas)

    for idx in range(count):
        row, col = divmod(idx, columns)
        x0 = col * digit_size
        y0 = row * (digit_size + padding)
        digit = Image.fromarray(images[idx], mode="L").resize(
            (digit_size, digit_size), resample=Image.Resampling.NEAREST
        )
        canvas.paste(digit, (x0, y0))
        draw.text((x0, y0 + digit_size + 2),
                  f"label={int(labels[idx])}", fill=0)

    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination)
    print(f"Saved preview image: {destination}")


def partition_by_digit(labels: np.ndarray) -> dict[int, np.ndarray]:
    return {digit: np.where(labels == digit)[0] for digit in range(10)}


def main() -> None:
    x_train, y_train, x_test, y_test = load_mnist()

    print(f"Training images shape: {x_train.shape}")
    print(f"Training labels shape: {y_train.shape}")
    print(f"Test images shape: {x_test.shape}")
    print(f"Test labels shape: {y_test.shape}")

    create_preview_grid(x_train, y_train, PREVIEW_PATH)

    digits = {d: x_train[y_train == d] for d in range(10)}
    digits_flat = {k: digits[k].reshape(
        digits[k].shape[0], 28 * 28) for k in range(10)}

    digits_flat[0].shape

    # train_partitions = partition_by_digit(y_train)
    # test_partitions = partition_by_digit(y_test)
    # print("\nTraining examples per digit:")
    # for digit in range(10):
    #     print(f"  {digit}: {len(train_partitions[digit])}")

    # print("\nTest examples per digit:")
    # for digit in range(10):
    #     print(f"  {digit}: {len(test_partitions[digit])}")

    # sample_digit = 7
    # sample_indices = train_partitions[sample_digit][:10]
    # print(f"\nFirst 10 training indices for digit {sample_digit}: {sample_indices.tolist()}")


if __name__ == "__main__":
    main()
