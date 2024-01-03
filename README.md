# CodeInsight Analyzer

CodeInsight Analyzer is a Python script designed to provide valuable insights into your code repository. By analyzing language usage, coding patterns, and project structure, this tool helps you make informed decisions, optimize collaboration, and enhance your development workflow.

## Planned Features

- [ ] **Swift Analysis**: Quickly traverse through your codebase to generate instant insights.
- [x] **Language Usage**: Identify the most prevalent programming languages in your repository.
- [ ] **Coding Patterns**: Highlight common coding patterns and structures.
- [ ] **Project Structure**: Get a clear overview of your project's organization.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Zilonis123/CodeInsight-Analyzer && cd CodeInsight-Analyzer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

```bash
python main.py <directory_path>
```

Replace `<directory_path>` with the path to your code repository.

## Configuration

- Customize the `exclude.json` file to specify folders or files you want to exclude from the analysis, but be precise because the names are case sensitive.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Contributions

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).