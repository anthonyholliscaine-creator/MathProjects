document.addEventListener("DOMContentLoaded", async () => {
  const codeNodes = document.querySelectorAll("[data-code-src]");
  const slideshowImages = document.querySelectorAll(".slideshow-image");
  const slideshowDots = document.querySelectorAll(".slideshow-dot");

  for (const node of codeNodes) {
    const source = node.getAttribute("data-code-src");
    if (!source) {
      continue;
    }

    try {
      const response = await fetch(source);
      if (!response.ok) {
        throw new Error(`Could not load ${source}`);
      }

      node.textContent = await response.text();

      if (window.Prism) {
        window.Prism.highlightElement(node);
      }
    } catch (error) {
      node.textContent =
        "# Unable to load the example code.\n" +
        "# If you opened this file directly, try serving the site locally.\n" +
        `# Missing source: ${source}`;
    }
  }

  if (slideshowImages.length > 1 && slideshowDots.length === slideshowImages.length) {
    let activeIndex = 0;

    window.setInterval(() => {
      slideshowImages[activeIndex].classList.remove("is-active");
      slideshowDots[activeIndex].classList.remove("is-active");

      activeIndex = (activeIndex + 1) % slideshowImages.length;

      slideshowImages[activeIndex].classList.add("is-active");
      slideshowDots[activeIndex].classList.add("is-active");
    }, 3200);
  }
});
