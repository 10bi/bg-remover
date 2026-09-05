from io import BytesIO
import os

from flask import Flask, render_template, request, send_file
from PIL import Image
from rembg import remove


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/remove-background", methods=["POST"])
def remove_background():
    uploaded_file = request.files.get("image")

    if uploaded_file is None or uploaded_file.filename == "":
        return "Please select an image.", 400

    try:
        input_image = Image.open(uploaded_file.stream)
        output_image = remove(input_image)

        output_buffer = BytesIO()
        output_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        return send_file(
            output_buffer,
            mimetype="image/png",
            as_attachment=True,
            download_name="background-removed.png",
        )

    except Exception:
        return "Unable to process the image.", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
