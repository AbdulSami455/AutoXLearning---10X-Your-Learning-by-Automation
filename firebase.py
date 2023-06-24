import pyrebase


firebaseConfig={

    "apiKey": "AIzaSyD5024GOHIfnQq5TJkOAznvQhNmXjMYED0",
    "authDomain": "autox-authentication.firebaseapp.com",
    "projectId": "autox-authentication",
    "storageBucket": "autox-authentication.appspot.com",
    "messagingSenderId": "513632417553",
    "appId": "1:513632417553:web:0102726d0828e4655ebeb0",
    "measurementId": "G-FRSHRYD8SE"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()


print("Hello")