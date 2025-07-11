import random

from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Circle Drawer</title></head>
<body>
<canvas id="canvas" width="600" height="400" style="border:1px solid #000;"></canvas>
<button onclick="drawCircle()">Draw Circle</button>
<script>
let ctx = document.getElementById("canvas").getContext("2d");
function drawCircle() {
    let x = Math.random() * 550 + 25;
    let y = Math.random() * 350 + 25;
    let r = Math.random() * 30 + 10;
    let colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink'];
    let color = colors[Math.floor(Math.random() * colors.length)];
    ctx.beginPath();
    ctx.arc(x, y, r, 0, 2 * Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.stroke();
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
