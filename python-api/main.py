from flask import Flask, request, jsonify
import yfinance as yf
import time

app = Flask(__name__)

@app.route("/candles/<ticker>")
def get_candles(ticker):
    range_ = request.args.get("range", "3mo")
    interval = request.args.get("interval", "1d")

    try:
        ticker_data = yf.Ticker(ticker)
        df = ticker_data.history(period=range_, interval=interval)

        currency = ticker_data.info.get("currency", "USD")
        if df.empty:
            return jsonify([])

        candles = []
        for ts, row in df.iterrows():
            candles.append({
                "time": int(ts.timestamp()),  # Convert to UNIX time
                "open": round(row["Open"], 2),
                "high": round(row["High"], 2),
                "low": round(row["Low"], 2),
                "close": round(row["Close"], 2),
                "volume": int(row["Volume"])
            })

        return jsonify({
            "currency": currency,
            "candles": candles
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000)
