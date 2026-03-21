document.addEventListener("DOMContentLoaded", async () => {
  const codeNodes = document.querySelectorAll("[data-code-src]");

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
});
