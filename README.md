# OpenGL Shapes Rendering Project

## Overview
This repository demonstrates the rendering of various shapes (square, triangle, and trapezoid) using OpenGL and Python. It utilizes the Pygame library for window management and event handling, and OpenGL for graphics rendering. Each shape is rendered with its own shaders and textures.

## Features
- **Shape Rendering**: Square, triangle, and trapezoid are rendered using vertex data and shaders.
- **Texture Mapping**: A wood texture is applied to each shape.
- **Shaders**: Vertex and fragment shaders are used for rendering.
- **Dynamic File Paths**: File paths are dynamically resolved using `__file__` for portability.

## File Structure
- `square/main.py`: The main entry point for rendering a square.
- `triangle/main.py`: The main entry point for rendering a triangle.
- `trapezoid/main.py`: The main entry point for rendering a trapezoid.
- `shaders/vertex.txt`: Vertex shader source code (used by all shapes).
- `shaders/fragment.txt`: Fragment shader source code (used by all shapes).
- `gfx/wood.jpg`: Texture file used for all shapes.

## Requirements
- Python 3.8 or higher
- Pygame
- PyOpenGL
- NumPy

## How to Run
1. Install the required Python packages:
   ```bash
   pip install pygame PyOpenGL numpy
   ```
2. Navigate to the folder of the shape you want to render (e.g., `square`, `triangle`, or `trapezoid`).
3. Run the `main.py` file:
   ```bash
   python main.py
   ```

## Acknowledgements
This project was inspired by tutorials from [Get Into Game Dev](https://www.youtube.com/@GetIntoGameDev). Special thanks for their valuable insights into game development and OpenGL rendering.

## License
This project is open-source and available under the MIT License.