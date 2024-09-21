

### Local Setup
```
# Creating local virtual environment to install python packages
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
cd rns

# Run the app
python manage.py runserver 0.0.0.0:80
```

You should now be able to access the upload form at localhost/upload

---

### Test Instructions
- Django route that takes a file upload, creates a new key, encrypts the file and stores in S3 (or file system)
