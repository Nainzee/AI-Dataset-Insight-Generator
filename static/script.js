function uploadDataset() {
  const fileInput = document.getElementById("fileInput");
  const analyzeBtn = document.getElementById("analyzeBtn");
  const loadingIndicator = document.getElementById("loadingIndicator");
  const errorMessage = document.getElementById("errorMessage");
  const resultsDiv = document.getElementById("results");

  const file = fileInput.files[0];

  if (!file) {
    showError("Please select a CSV file before clicking Analyze Dataset.");
    return;
  }

  // Clear previous state
  errorMessage.style.display = "none";
  errorMessage.innerText = "";
  resultsDiv.innerHTML = "";

  // Show loading state
  loadingIndicator.style.display = "flex";
  analyzeBtn.disabled = true;
  analyzeBtn.classList.add("disabled");
  analyzeBtn.innerText = "Analyzing...";

  const formData = new FormData();
  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then(async (res) => {
      const data = await res.json().catch(() => null);
      if (!res.ok) {
        const errorDetail = (data && data.error) ? data.error : `Server error (${res.status})`;
        throw new Error(errorDetail);
      }
      return data;
    })
    .then((data) => {
      if (!Array.isArray(data) || data.length === 0) {
        showError("No visual charts or insights could be generated for this dataset.");
        return;
      }

      data.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";

        const title = document.createElement("h3");
        title.innerText = item.column;

        const type = document.createElement("div");
        type.className = "chart-badge";
        type.innerText = item.chart_type.toUpperCase();

        const imgWrapper = document.createElement("div");
        imgWrapper.className = "chart-wrapper";

        const img = document.createElement("img");
        // Add cache buster timestamp so newly generated plots reload immediately
        img.src = "/charts/" + encodeURIComponent(item.chart) + "?t=" + new Date().getTime();
        img.alt = item.column + " chart";
        img.loading = "lazy";

        imgWrapper.appendChild(img);

        const insightBox = document.createElement("div");
        insightBox.className = "insight-box";

        const insightLabel = document.createElement("strong");
        insightLabel.innerText = "💡 AI Insight:";

        const insightText = document.createElement("p");
        insightText.innerText = item.insight;

        insightBox.appendChild(insightLabel);
        insightBox.appendChild(insightText);

        card.appendChild(title);
        card.appendChild(type);
        card.appendChild(imgWrapper);
        card.appendChild(insightBox);

        resultsDiv.appendChild(card);
      });
    })
    .catch((err) => {
      showError(err.message || "An unexpected error occurred while analyzing the dataset.");
    })
    .finally(() => {
      loadingIndicator.style.display = "none";
      analyzeBtn.disabled = false;
      analyzeBtn.classList.remove("disabled");
      analyzeBtn.innerText = "Analyze Dataset";
    });
}

function showError(msg) {
  const errorMessage = document.getElementById("errorMessage");
  errorMessage.innerText = msg;
  errorMessage.style.display = "block";
}
