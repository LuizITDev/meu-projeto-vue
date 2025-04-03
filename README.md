# meu-projeto-vue
Health Plan Operator Search Application

This project is a web-based application built using Vue.js for the front end and Python (FastAPI) for the back end. The goal of this application is to provide an easy-to-use interface for searching health plan operators using a CSV dataset provided by the Brazilian National Health Agency (ANS).

Features:
	1.	Search Functionality:
	•	Users can search for health operators by name through a search bar.
	•	The application interacts with a FastAPI back-end server that performs a search on the CSV dataset containing registered health operators’ information.
	2.	Data Display:
	•	After searching, the results are displayed in a clean and simple list format, showing essential information like the operator’s name, CNPJ, and other details.
	•	When a user clicks on an operator name, more detailed information about that operator is shown.
	3.	Interactive Front End:
	•	The front-end is built using Vue.js, offering a dynamic user experience.
	•	Responsive design with minimal styling for easy navigation and use.
	4.	Backend API (FastAPI):
	•	A Python server running FastAPI that interacts with the CSV data.
	•	The server processes requests, performs text searches in the operator data, and returns relevant results as a JSON response.

Technical Stack:
	•	Frontend: Vue.js (for building the user interface)
	•	Backend: Python (FastAPI for API handling)
	•	Database: CSV file containing health operators’ data
	•	HTTP Requests: Axios (for making API calls from Vue.js)

How It Works:
	•	The user enters a search term in the search bar.
	•	The front end sends a GET request to the FastAPI server, which processes the search term and queries the CSV file for matching operators.
	•	The server sends back the relevant search results, which are displayed in the front end.

Project Goal:

The project aims to simplify the process of finding health insurance providers (operators) using an intuitive and interactive web application. It provides users with a direct and effective way to search for operator information from an official dataset.
