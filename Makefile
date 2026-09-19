# ╔══════════════════════════════════════════════════════════════╗
# ║                    EXPENSE TRACKER                           ║
# ║              Flask Development Makefile                      ║
# ╚══════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────────
# ⚙️  Configuration
# ────────────────────────────────────────────────────────────────

PYTHON := python
UV := uv


# ────────────────────────────────────────────────────────────────
# 📦 Installation & Dependencies
# ────────────────────────────────────────────────────────────────

## Install all project dependencies
install:
	$(UV) sync

## Install production dependencies only
install-prod:
	$(UV) sync --no-dev

## Upgrade dependencies
upgrade:
	$(UV) lock --upgrade
	$(UV) sync


# ────────────────────────────────────────────────────────────────
# 🚀 Flask Application
# ────────────────────────────────────────────────────────────────

## Run the Flask application in development mode
run:
	$(UV) run flask --app expense_tracker.app run --debug

## Run Flask on all network interfaces
run-host:
	$(UV) run flask --app expense_tracker.app run --debug --host=0.0.0.0

## Run Flask on a custom port
run-port:
	$(UV) run flask --app expense_tracker.app run --debug --port=8000


# ────────────────────────────────────────────────────────────────
# 🧪 Testing
# ────────────────────────────────────────────────────────────────

## Run all tests
test:
	$(UV) run pytest

## Run tests with verbose output
test-verbose:
	$(UV) run pytest -v


# ────────────────────────────────────────────────────────────────
# 🔍 Linting & Formatting
# ────────────────────────────────────────────────────────────────

## Check code for linting errors
lint:
	$(UV) run ruff check .

## Automatically fix linting errors
lint-fix:
	$(UV) run ruff check . --fix

## Format the entire codebase
format:
	$(UV) run ruff format .

## Check formatting without modifying files
format-check:
	$(UV) run ruff format . --check

## Run linting and formatting
check:
	$(UV) run ruff check .
	$(UV) run ruff format . --check

## Fix linting and format the entire codebase
fix:
	$(UV) run ruff check . --fix
	$(UV) run ruff format .


# ────────────────────────────────────────────────────────────────
# 🧹 Cleanup
# ────────────────────────────────────────────────────────────────

## Remove Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

## Remove pytest cache
clean-pytest:
	rm -rf .pytest_cache

## Remove Ruff cache
clean-ruff:
	rm -rf .ruff_cache

## Remove all generated caches
clean-all: clean clean-pytest clean-ruff


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
	@echo "  make install-prod  Install production dependencies"
	@echo "  make upgrade       Upgrade dependencies"
	@echo ""
	@echo "  make run           Run Flask application"
	@echo "  make run-host      Run Flask on all interfaces"
	@echo "  make run-port      Run Flask on port 8000"
	@echo ""
	@echo "  make test          Run tests"
	@echo "  make test-verbose  Run tests with verbose output"
	@echo ""
	@echo "  make lint          Check linting"
	@echo "  make lint-fix      Fix linting errors"
	@echo "  make format        Format code"
	@echo "  make format-check  Check formatting"
	@echo "  make check         Run lint + format check"
	@echo "  make fix           Fix lint + format"
	@echo ""
	@echo "  make clean         Remove Python cache"
	@echo "  make clean-pytest  Remove pytest cache"
	@echo "  make clean-ruff    Remove Ruff cache"
	@echo "  make clean-all     Remove all caches"
	@echo ""