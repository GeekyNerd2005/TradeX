from flask import Flask, request, jsonify
import yfinance as yf
import time

app = Flask(__name__)

import time

@app.route("/candles/<ticker>")
def get_candles(ticker):
    range_ = request.args.get("range", "3mo")
    interval = request.args.get("interval", "1d")

    try:
        df = yf.Ticker(ticker).history(period=range_, interval=interval)

        if df.empty:
            return jsonify({"candles": [], "currency": "INR"})

        # Add a 'time' column in UNIX seconds
        df["time"] = df.index.map(lambda x: int(time.mktime(x.timetuple())))

        # Rename the columns to lowercase just in case
        df = df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        })

        df = df.reset_index(drop=True)

        candles = df[["time", "open", "high", "low", "close", "volume"]].to_dict(orient="records")

        return jsonify({
            "currency": "INR",
            "candles": candles
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8000)
