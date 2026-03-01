# Learning Objectives for This Project

Based on the attached files, this is a **GitHub Copilot learning project** designed to teach you advanced Copilot techniques in a practical context. Here are the key learning outcomes:

## 1. **Interactive Code Generation with Copilot**
The project demonstrates how to use GitHub Copilot's inline chat (`Ctrl+I` on Windows, `Cmd+I` on Mac) to generate code interactively. Rather than writing code from scratch, you learn to:
- Use natural language prompts to describe what you want
- Refine prompts iteratively until the result meets your needs
- Collaborate with AI on code generation

## 2. **Building RESTful APIs with FastAPI**
You'll gain practical experience with:
- Creating API endpoints using FastAPI decorators (`@app.get()`)
- Path parameters for dynamic routes (e.g., `{country}`, `{city}`, `{month}`)
- Returning JSON responses
- Error handling (HTTP 404 exceptions)

## 3. **Test-Driven Development with Copilot**
The project teaches you to:
- Write unit tests using pytest
- Use Copilot Chat to generate tests alongside feature code
- Validate edge cases (e.g., non-existent countries returning 404)
- Iterate on tests when they don't work correctly

## 4. **Python Best Practices**
Following the conventions in [python.instructions.md](.github/instructions/python.instructions.md), you'll learn:
- PEP 8 style guidelines
- Type hints and docstrings
- Clear function documentation
- Code readability and maintainability

## 5. **Using Workspace/Agent Features**
The final exercise introduces **Copilot Workspace** (`@workspace` agent) for:
- Generating project documentation
- Writing README files
- Understanding how AI agents can help with higher-level tasks beyond code generation

## 6. **DevContainer & Local Development**
The project shows how to:
- Set up reproducible development environments
- Use Docker for consistent Python environments
- Configure VS Code with Copilot extensions
- Run servers locally with hot-reload (uvicorn)

## The Practical Exercise

The three-step exercise in the README guides you through:
1. **Creating a new route** - `GET /countries/{country}` to list cities
2. **Writing tests** - Ensuring your route works correctly
3. **Documenting with Copilot** - Using the workspace agent to improve documentation

## Key Takeaway

This project teaches you that **GitHub Copilot isn't just a code completion tool**—it's a collaborative partner for:
- Rapid prototyping
- Test generation
- Documentation creation
- Iterative refinement of solutions

You'll learn to work *with* Copilot through conversation, prompts, and feedback loops, making you a more productive developer.
