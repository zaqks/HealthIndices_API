function uploadImages(dataUrls, uploadUrl, onComplete) {
  // Create a FormData object
  const formData = new FormData();

  // Convert each data URL to a blob and add it to FormData
  const blobPromises = dataUrls.map((dataUrl, index) => {
    return fetch(dataUrl)
      .then((response) => response.blob())
      .then((blob) => {
        formData.append(`image${index}`, blob);
      })
      .catch((error) =>
        console.error("Error converting data URL to blob:", error)
      );
  });

  // Wait for all blobs to be created and then send the request
  Promise.all(blobPromises).then(() => {
    // Send the AJAX request
    fetch(uploadUrl, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => onComplete(data))
      .catch((error) => console.error("Error uploading images:", error));
  });
}
