class WebCam {
  constructor(cam_id) {
    this.root = document.getElementById(cam_id).children[1];
    this.video = this.root.children[0];
    //
    this.canvas = this.root.children[1];
    this.ctx = this.canvas.getContext("2d");

    this.btn = this.root.children[2];
    this.preview = false;
    //
    this.enable_camera();

    // EVENT
    this.btn.addEventListener("click", () => this.take_pic());
    this.data = null;
  }

  enable_camera() {
    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
          this.video.srcObject = stream;
        })
        .catch((error) => {
          console.error("Error accessing webcam:", error);
        });
    } else console.log("getUserMedia not supported");
  }

  toggle_preview() {
    this.preview = !this.preview;
    this.root.classList.toggle("preview");
  }

  take_pic() {
    this.toggle_preview();

    if (this.preview) {
      // Get video dimensions
      const videoWidth = this.video.videoWidth;
      const videoHeight = this.video.videoHeight;

      // Set canvas dimensions to match video dimensions
      this.canvas.width = videoWidth;
      this.canvas.height = videoHeight;

      // Draw video frame onto canvas
      this.ctx.drawImage(
        this.video,
        0, // Source x
        0, // Source y
        videoWidth, // Source width
        videoHeight, // Source height
        0, // Destination x
        0, // Destination y
        videoWidth, // Destination width
        videoHeight // Destination height
      );

      // // Save image as a data URL
      // const imageDataURL = this.canvas.toDataURL("image/png");
      this.data = this.canvas.toDataURL("image/png");

      // // Create a download link
      // const link = document.createElement("a");
      // link.href = imageDataURL;
      // link.download = "webcam_photo.png";
      // link.click();
    }
  }
  //
}
