<!DOCTYPE html>
<html>
<head>
    <title>Neshmi's Lab 3.9 App</title>
</head>
<body>
    <h2>Add Contact - Lab 3.9 by Neshmi</h2>
    <form method="POST" action="/">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <label for="phone">Phone Number:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>
        <input type="submit" value="Submit">
    </form>
    <p>{{ message }}</p>
    {% if contacts %}
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Phone Number</th>
            </tr>
            {% for contact in contacts %}
                <tr>
                    <td>{{ contact['id'] }}</td>
                    <td>{{ contact['name'] }}</td>
                    <td>{{ contact['phone'] }}</td>
                </tr>
            {% endfor %}
        </table>
    {% else %}
        <p>No contacts found.</p>
    {% endif %}
    <p>App built by Neshmi Alhayek for CIT 225 - Lab 3.9</p>
</body>
</html>
