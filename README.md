<!DOCTYPE html>
<html>
<body>
  <h1>Ride Request Service</h1>
  
  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.6+</li>
    <li>Django 3.1+</li>
    <li>Django REST Framework 3.12+</li>
  </ul>
  
  <h2>Getting Started</h2>
  <ol>
    <li>Clone the repository:</li>
    <code>git clone https://github.com/adit-dubey/Ride-Request-Service.git</code>
    <li>Navigate to the project directory:</li>
    <code>cd Ride-Request-Service</code>
    <li>Install the dependencies:</li>
    <code>pip install -r requirements.txt</code>
    <li>Apply database migrations:</li>
    <code>python manage.py migrate</code>
    <li>Start the development server:</li>
    <code>python manage.py runserver</code>
  </ol>
  
  <h2>API Documentation</h2>
  <p>
    Once the development server is running, you can explore the API endpoints using a tool like cURL or an API testing tool like Postman. The API documentation is available at <code>http://localhost:8000/docs/</code>.
  </p>
  
  <h2>Notes</h2>
  <ul>
    <li>
      The application uses Django's built-in authentication system for user registration and authentication. You can register a new user by sending a POST request to <code>/api/register/</code>. After registering, you can obtain an authentication token by sending a POST request to <code>/api/token/</code>. Include the token in the <code>Authorization</code> header for authenticated requests.
    </li>
    <li>
      The application uses SQLite as the default database. If you want to use a different database, update the database settings in the <code>settings.py</code> file.
    </li>
    <li>
      Make sure to set appropriate values for the <code>SECRET_KEY</code> and <code>DEBUG</code> settings in the <code>settings.py</code> file for production deployments.
    </li>
    <li>
      Customize and extend the functionality of the API according to your specific requirements by modifying the existing code or adding new endpoints.
    </li>
  </ul>
  
  <h2>Contributing</h2>
  <p>
    Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
  </p>
  
  <h2>License</h2>
  <p>
    This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.
  </p>
</body>
</html>
