from flask import Flask, render_template, request

app = Flask(__name__)

# Company information stored in dictionaries (instead of database)
company_info = {
    "name": "TechSolutions Inc.",
    "tagline": "Innovative Solutions for Tomorrow's Challenges",
    "founded": 2015,
    "employees": 45,
    "about": "TechSolutions Inc. is a forward-thinking technology company dedicated to providing cutting-edge solutions to businesses of all sizes. With our team of experienced professionals, we combine technical expertise with innovative thinking to deliver results that exceed expectations."
}

company_services = [
    {
        "id": 1,
        "name": "Web Development",
        "description": "Custom web applications tailored to your business needs using the latest technologies and frameworks.",
        "icon": "code"
    },
    {
        "id": 2,
        "name": "Mobile App Development",
        "description": "Native and cross-platform mobile applications for iOS and Android devices.",
        "icon": "apple"
    },
    {
        "id": 3, 
        "name": "Cloud Solutions",
        "description": "Scalable cloud infrastructure setup, migration, and management services.",
        "icon": "cloud"
    },
    {
        "id": 4,
        "name": "IT Consulting",
        "description": "Strategic technology guidance to help your business grow and innovate.",
        "icon": "briefcase"
    }
]

team_members = [
    {
        "id": 1,
        "name": "Vasim Antule",
        "position": "CEO & Founder",
        "bio": "With over 15 years of experience in tech industry leadership."
    },
    {
        "id": 2,
        "name": "Vikas Temkar",
        "position": "CTO",
        "bio": "Expert in cloud architecture and software development."
    },
    {
        "id": 3,
        "name": "Ajaj Mujawar",
        "position": "Lead Developer",
        "bio": "Full-stack developer with a passion for clean, efficient code."
    }
]

contact_info = {
    "address": "123 Tech Boulevard, Innovation City, TX 75001",
    "phone": "+91 9112093342",
    "email": "info@techsolutions.net",
    "social_media": {
        "twitter": "https://twitter.com/techsolutions",
        "linkedin": "https://linkedin.com/company/techsolutions",
        "facebook": "https://facebook.com/techsolutions"
    }
}

# Routes
@app.route('/')
def home():
    return render_template('index.html', 
                          company=company_info, 
                          services=company_services,
                          team=team_members,
                          contact=contact_info)

@app.route('/about')
def about():
    return render_template('about.html', 
                          company=company_info,
                          team=team_members)

@app.route('/services')
def services():
    return render_template('services.html', 
                          company=company_info,
                          services=company_services)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message_sent = False
    if request.method == 'POST':
        # In a real application, you would process the form data here
        # For example, send an email, store the message, etc.
        message_sent = True
    
    return render_template('contact.html', 
                          company=company_info,
                          contact=contact_info,
                          message_sent=message_sent)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = next((s for s in company_services if s["id"] == service_id), None)
    if service:
        return render_template('service_detail.html', 
                              company=company_info,
                              service=service)
    return "Service not found", 404

if __name__ == '__main__':
    app.run(debug=True)