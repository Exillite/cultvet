# API documentation

## Models

### **User**
- id - str
- tg_id - int
- points - int

### **Question**
- id - str
- title - str
- answers - [str]
- correct_answers - [str]

### **EcscursionPart**
- id - str
- title - str
- audio - str
- materials - [url]
- is_test - bool
- test - [Question]

### **Ecscursion**
- id - str
- author - User
- title - str
- description - str
- preview_img - url
- nead_time - int
- distance - int
- route_url - url
- parts - [EcscursionPart]

### **PassEcscursion**
- id - str
- user - User
- ecscursion - Ecscursion
- is_finished - bool
- start_time - datetime
- finish_time - datetime
- correct_answers - int
- points - int


## Methods

### Register New User
- **Endpoint:** `users/register`
- **Method:** POST
- **Description:** Registers a new user in the system.

### Get User
- **Endpoint:** `/users/{user_id}`
- **Method:** GET
- **Description:** Retrieves details about a specific user.

### Get User by Telegram ID
- **Endpoint:** `/users/tg/{tg_id}`
- **Method:** GET
- **Description:** Retrieves details about a user using their Telegram ID.

### Update Excursion Pass
- **Endpoint:** `/users/{user_id}`
- **Method:** PUT
- **Description:** Updates details of an existing user.

### Get All Excursions
- **Endpoint:** `/excursions`
- **Method:** GET
- **Description:** Retrieves a list of all available excursions.

### Get Excursion
- **Endpoint:** `/excursions/{excursion_id}`
- **Method:** GET
- **Description:** Retrieves details about a specific excursion.

### Create New Excursion
- **Endpoint:** `/excursions`
- **Method:** POST
- **Description:** Creates a new excursion in the system.

### Update Excursion
- **Endpoint:** `/excursions/{excursion_id}`
- **Method:** PUT
- **Description:** Updates details of an existing excursion.

### Create New Excursion Pass
- **Endpoint:** `/excursionspass`
- **Method:** POST
- **Description:** Creates a new excursion pass for a user.

### Update Excursion Pass
- **Endpoint:** `/excursionspass/{pass_id}`
- **Method:** PUT
- **Description:** Updates details of an existing excursion pass.

### Add Correct answer
- **Endpoint:** `/excursionspass/{pass_id}/correctanswer`
- **Method:** POST