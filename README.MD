
# TRADEX - Paper Trading Terminal

A full-stack plug-and-play trading terminal that simulates real-time trading with market, limit, stop, and advanced order types — complete with charting, portfolio tracking, and order matching. Inspired by platforms like Groww, Zerodha, and TradingView.

##  Monorepo Structure

```bash
tradex/
├── backend/           # .NET 9 Web API (order matching, portfolio, auth)
├── frontend/          # React + Tailwind terminal UI (candles, forms, dashboard)
├── market-data/       # Python Flask APIs for real-time price and candle data
│   ├── main.py        # Candle data via yFinance
│   └── market_api.py  # Live price via yFinance (fast_info + fallback)
└── README.md          # This file
```

---

## Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/tradex.git
cd tradex
```

---

## Setup Instructions

### Frontend (`React`)

```bash
cd ../frontend
npm install
npm start
```

Runs on [http://localhost:3000](http://localhost:3000)  
Ensure `.env` contains:

```
REACT_APP_BACKEND_URL=http://localhost:5001
```

---

### Backend (`.NET 9` API)

```bash
cd backend
dotnet restore
dotnet ef database update
dotnet run
```

Runs on [http://localhost:5001](http://localhost:5001)

**.env (or `appsettings.json`) should contain:**

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Host=localhost;Database=tradex;Username=your_user;Password=your_pass"
  },
  "Jwt": {
    "Key": "your_jwt_secret",
    "Issuer": "tradex"
  }
}
```

---

### Python Market API (`Flask + yFinance`)

```bash
cd ../market-data
# Optionally create a virtual environment
pip install -r requirements.txt

# Start candle API
python main.py  # runs on :8000

# Start price API (separate terminal)
python market_api.py  # runs on :5050

```

Runs on [http://localhost:8000](http://localhost:8000)

Endpoints:
-GET /candles/<ticker>?range=3mo&interval=1d
→ returns [{ time, open, high, low, close, volume }]

GET /price?ticker=INFY.NS
→ returns { ticker, price, currency }

---
Tech Stack

Frontend: React, Tailwind, Lightweight Charts, Axios, SignalR
Backend: ASP.NET Core 9, Entity Framework Core, PostgreSQL
Market Data: Python + Flask + yFinance
Theme: Dark/Light toggle with Rajdhani & Orbitron fonts
Design: Groww-style, responsive layout, realtime updates

---

## Features

-  Candlestick charts (1mo, 3mo, 6mo, 1y, max)
-  Place market, limit, stop orders
-  Real-time WebSocket updates (price, portfolio, order book)
-  Portfolio tracking (P&L, average buy price, pie chart)
-  Risk checks (max position, basic margin)
-  Light/Dark mode toggle
-  User registration, login, and JWT-based auth
-  Indicators: EMA, RSI, MACD
-  Seed mock users/trades for realism

---

##  Example `.env.template` Files

### `frontend/.env.template`
```
REACT_APP_BACKEND_URL=http://localhost:5001
```

### `backend/appsettings.Development.json`
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Host=localhost;Database=tradex;Username=your_user;Password=your_pass"
  },
  "Jwt": {
    "Key": "your_secret_key",
    "Issuer": "tradex"
  }
}
```

---

## Technologies

- **Frontend:** React, Tailwind, Lightweight Charts, SignalR client
- **Backend:** ASP.NET Core 9, EF Core, SQLLite, SignalR, JWT
- **Market API:** Flask, yFinance, Pandas, NumPy

---

## Coming Soon

-  Options & futures module
-  Risk dashboards
-  Technical drawing tools on chart
-  Plug-and-play Docker support

---

##  Credits

Built with ♥ by Sasmit Jha 
Inspired by real-world terminals and financial platforms.

---


