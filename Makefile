# ╔══════════════════════════════════════════════════════════════╗
# ║                    EXPENSE TRACKER                          ║
# ║              Flask Development Makefile                    ║
# ╚══════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────────
# ⚙️  Configuration
# ────────────────────────────────────────────────────────────────

PYTHON := python
PIP := $(PYTHON) -m pip


# ────────────────────────────────────────────────────────────────
# 📦 Installation & Dependencies
# ────────────────────────────────────────────────────────────────

## Install all project dependencies
install:
	$(PIP) install -r requirements.txt

## Upgrade pip
upgrade-pip:
	$(PIP) install --upgrade pip


# ────────────────────────────────────────────────────────────────
# 🚀 Flask Application
# ────────────────────────────────────────────────────────────────

## Run the Flask application in development mode
run:
	flask --app app run --debug

## Run Flask on all network interfaces
run-host:
	flask --app app run --debug --host=0.0.0.0

## Run Flask on a custom port
run-port:
	flask --app app run --debug --port=8000


# ────────────────────────────────────────────────────────────────
# 🧪 Testing
# ────────────────────────────────────────────────────────────────

## Run all tests
test:
	pytest

## Run tests with verbose output
test-verbose:
	pytest -v


# ────────────────────────────────────────────────────────────────
# 🧹 Cleanup
# ────────────────────────────────────────────────────────────────

## Remove Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

## Remove pytest cache
clean-pytest:
	rm -rf .pytest_cache


# ────────────────────────────────────────────────────────────────
# ℹ️  Help
# ────────────────────────────────────────────────────────────────

## Display available commands
help:
	@echo ""
	@echo "Expense Tracker - Available Commands"
	@echo "====================================="
	@echo ""
	@echo "  make install       Install dependencies"
	@echo "  make upgrade-pip   Upgrade pip"
	@echo ""
	@echo "  make run           Run Flask application"
	@echo "  make run-host      Run Flask on all interfaces"
	@echo "  make run-port      Run Flask on port 8000"
	@echo ""
	@echo "  make test          Run tests"
	@echo "  make test-verbose  Run tests with verbose output"
	@echo ""
	@echo "  make clean         Remove Python cache"
	@echo "  make clean-pytest  Remove pytest cache"
	@echo ""