from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route("/price", methods=["GET"])
def get_price():
    ticker = request.args.get("ticker")
    if not ticker:
        return jsonify({"error": "Ticker required"}), 400

    try:
        data = yf.Ticker(ticker)
        
        price = data.fast_info.get("last_price")
        currency = data.fast_info.get("currency") 

        if price is None:
            hist = data.history(period="1d", interval="1m")
            if hist.empty:
                return jsonify({"error": "Price history not available"}), 404
            price = hist["Close"].iloc[-1]

        if currency is None:
            currency = data.info.get("currency", "USD")

        return jsonify({
            "ticker": ticker,
            "price": price,
            "currency": currency
        })
    except Exception as e:
        print(f"Exception: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
