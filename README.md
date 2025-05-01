# Flask Interactive Charts

A web application built with Flask that displays interactive charts using Chart.js. It allows real-time visualization of dynamic data with a modern and responsive interface. Includes a REST API for data retrieval and an intuitive design for information visualization.

## Features

- Interactive bar chart with Chart.js
- Real-time data updates
- Responsive and modern design with CSS3
- Intuitive user interface
- REST API for random data
- Easy to customize and extend

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ksalapeg/flask-interactive-charts.git
cd flask-interactive-charts
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
flask-interactive-charts/
├── app.py              # Main Flask application file
├── requirements.txt    # Project dependencies
├── .gitignore         # Git ignored files and directories
├── LICENSE            # MIT License
└── templates/         # Templates directory
    └── index.html     # Main template with chart
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Main Components

### app.py
- Flask application configuration
- Main route ('/') for page rendering
- API route ('/datos') for random data
- Dynamic data generation

### templates/index.html
- Responsive user interface
- Chart.js implementation
- Integrated CSS styles
- JavaScript functionality for dynamic updates
- Modern and attractive design

## API Endpoints

### GET /datos
Returns random data in JSON format:
```json
{
    "labels": ["January", "February", "March", "April", "May"],
    "valores": [23, 45, 67, 89, 12]
}
```

## Technologies Used

- **Backend**:
  - Flask 3.0.2
  - Werkzeug 3.0.1

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
  - Chart.js

## Customization

### Modify Chart
To change the chart type, modify the `type` parameter in Chart.js configuration in `index.html`:
```javascript
type: 'bar' // Change to 'line', 'pie', etc.
```

### Change Data
To modify the generated data, edit the `obtener_datos()` function in `app.py`.

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

Kevin Alape - [ksalapeg.270700@gmail.com](mailto:ksalapeg.270700@gmail.com)

Project Link: [https://github.com/Khawk2/flask-interactive-charts](https://github.com/Khawk2/flask-interactive-charts)

