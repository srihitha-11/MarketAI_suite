from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    product = request.form['product']
    audience = request.form['audience']

    # --- Dummy AI Content ---
    description = f"{product} is an innovative solution designed for {audience}. \
It boosts productivity, engagement, and overall business growth."

    ads = [
        f"🚀 Boost your business with {product} today!",
        f"{product} – The smart choice for {audience}. Try now!",
        f"Experience the power of {product}. Start today!"
    ]

    videos = [
        "🎬 Animated cartoon explainer video showing product workflow",
        "🎤 AI voice-over demo video explaining benefits",
        "📱 Short social media reel with catchy animations"
    ]

    return render_template(
        'index.html',
        product=product,
        description=description,
        ads=ads,
        videos=videos
    )

if __name__ == "__main__":
    app.run(debug=True)
