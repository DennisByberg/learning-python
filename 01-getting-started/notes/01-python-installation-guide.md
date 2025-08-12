# Python Installation Setup

## On WSL/Linux (using pyenv)

### Install dependencies

```bash
sudo apt update
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev
```

### Install pyenv

```bash
curl https://pyenv.run | bash
```

### Configure shell

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

### Install Python 3.13.6 directly

```bash
# List available versions (optional)
pyenv install --list | grep 3.13

# Install latest version directly
pyenv install 3.13.6
pyenv global 3.13.6

# Verify installation
python --version
python3 --version
```

## On Windows/Mac/regular computer

Download Python directly from the official website:

- Go to [python.org](https://www.python.org/downloads/)
- Download the latest version (3.13.6)
- Follow the installation guide
- Make sure "Add Python to PATH" is checked

## Useful pyenv commands (for Linux/WSL)

- `pyenv versions` - List installed versions
- `pyenv install --list` - List available versions
- `pyenv local <version>` - Set version for specific project
- `pyenv global <version>` - Set global version
- `pyenv which python` - Show path to active Python
- `pyenv uninstall <version>` - Remove an installed version

## VS Code Setup

After Python installation:

1. Install Python extension in VS Code
2. Use **Ctrl+Shift+P** → "Python: Select Interpreter"
3. Select Python 3.13.6

## Cleanup

If you have multiple versions installed, you can remove old ones:

```bash
# Check installed versions
pyenv versions

# Remove old versions
pyenv
```
