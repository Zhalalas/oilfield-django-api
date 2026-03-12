# Oilfield API

A RESTful API for managing oilfield operations, including wells, sensors, and production readings. Built with Django and Django Ninja for high-performance API development.

## Features

- 🛢️ **Oil Field Management** - Create, read, update, and delete oil fields with operator information and location tracking
- ⚙️ **Well Monitoring** - Track well status (active, shut-in, abandoned), drilling dates, and depth measurements
- 📊 **Sensor Management** - Monitor sensors for pressure, temperature, and flow rate measurements across wells
- 📈 **Production Readings** - Collect and retrieve production data from sensors with timestamps and unit information
- 🐳 **Docker Support** - Fully containerized with PostgreSQL database
- 🔐 **Type-Safe APIs** - Built with Pydantic schemas for request/response validation
- ⚡ **Fast Performance** - Django Ninja provides near-ASGI performance improvements

## Tech Stack

- **Backend Framework**: [Django 6.0+](https://www.djangoproject.com/)
- **API Framework**: [Django Ninja 1.5+](https://django-ninja.rest-framework.com/)
- **Database**: PostgreSQL (via Docker Compose)
- **Python**: 3.12+
- **Package Manager**: [UV](https://astral.sh/blog/uv)

## Prerequisites

- Python 3.12 or higher
- Docker & Docker Compose (optional, for database)
- UV package manager (recommended) or pip

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/oilfield-api-django.git
cd oilfield-api-django
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```env
# Database Configuration
POSTGRES_USER=oilfield_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=oilfield_db
POSTGRES_PORT=5432

# Django Settings
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Install Dependencies

Using UV (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 4. Start the Database

```bash
docker-compose up -d
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. (Optional) Seed Sample Data

```bash
python manage.py seed_oilfield_data
```

## Running the Server

### Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

### Interactive API Documentation

Django Ninja automatically generates interactive API docs. Visit:

- **Swagger UI**: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
- **ReDoc**: [http://localhost:8000/api/redoc](http://localhost:8000/api/redoc)

## API Endpoints

### Oil Fields

- `POST /api/oil-fields/` - Create a new oil field
- `GET /api/oil-fields/` - List all oil fields
- `GET /api/oil-fields/{id}` - Get oil field details
- `PUT /api/oil-fields/{id}` - Update an oil field
- `DELETE /api/oil-fields/{id}` - Delete an oil field

### Wells

- `POST /api/wells/` - Create a new well
- `GET /api/wells/` - List all wells
- `GET /api/wells/{id}` - Get well details
- `PUT /api/wells/{id}` - Update a well
- `DELETE /api/wells/{id}` - Delete a well

### Sensors

- `POST /api/sensors/` - Create a new sensor
- `GET /api/sensors/` - List all sensors
- `GET /api/sensors/{id}` - Get sensor details
- `PUT /api/sensors/{id}` - Update a sensor
- `DELETE /api/sensors/{id}` - Delete a sensor

### Production Readings

- `POST /api/production-readings/` - Record a new production reading
- `GET /api/production-readings/` - List all readings
- `GET /api/production-readings/{id}` - Get reading details
- `PUT /api/production-readings/{id}` - Update a reading
- `DELETE /api/production-readings/{id}` - Delete a reading

## Data Models

### OilField

- `id` - Primary key
- `name` - Field name
- `location` - Geographic location
- `operator_company` - Operating company name
- `start_date` - Field start date

### Well

- `id` - Primary key
- `oil_field` - Foreign key to OilField
- `name` - Well name
- `status` - Well status (active, shut-in, abandoned)
- `drill_date` - Drilling date
- `depth_m` - Well depth in meters

### Sensor

- `id` - Primary key
- `well` - Foreign key to Well
- `sensor_type` - Type of sensor (pressure, temperature, flow_rate)
- `install_date` - Installation date
- `is_active` - Whether sensor is currently active

### ProductionReading

- `id` - Primary key
- `sensor` - Foreign key to Sensor
- `timestamp` - Reading timestamp
- `value` - Measured value
- `unit` - Unit of measurement

## Project Structure

```
.
├── api/                        # Django configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── asgi.py                # ASGI configuration
│   └── wsgi.py                # WSGI configuration
├── oilfield/                  # Main application
│   ├── models.py              # Data models
│   ├── schemas.py             # Pydantic schemas
│   ├── admin.py               # Django admin config
│   ├── routers/               # API route handlers
│   │   ├── oil_fields.py
│   │   ├── wells.py
│   │   ├── sensors.py
│   │   └── production_readings.py
│   ├── management/            # Django management commands
│   │   └── commands/
│   │       └── seed_oilfield_data.py
│   └── migrations/            # Database migrations
├── manage.py                  # Django management script
├── docker-compose.yaml        # Docker configuration
├── pyproject.toml             # Project metadata and dependencies
└── README.md                  # This file
```

## Development

### Running Tests

```bash
python manage.py test
```

### Making Database Changes

1. Update models in `oilfield/models.py`
2. Create migration:
   ```bash
   python manage.py makemigrations
   ```
3. Apply migration:
   ```bash
   python manage.py migrate
   ```

### Code Style

Ensure your code follows PEP 8 standards. Consider using:

- **Black** for code formatting
- **Flake8** for linting
- **isort** for import sorting

## Deployment

For production deployment:

1. Update `settings.py`:
   - Set `DEBUG = False`
   - Set proper `ALLOWED_HOSTS`
   - Generate a new `SECRET_KEY`
   - Configure a production database

2. Run migrations:

   ```bash
   python manage.py migrate --settings=api.settings
   ```

3. Collect static files:

   ```bash
   python manage.py collectstatic --noinput
   ```

4. Use a production WSGI server (Gunicorn, uWSGI, etc.)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please open an issue on GitHub or contact the project maintainers.

---

**Last Updated**: March 2026
