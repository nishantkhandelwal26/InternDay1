from flask import Flask, render_template, jsonify

app = Flask(__name__)

print(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'New York, NY',
        'salary': '100,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '120,000'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Austin, TX',
        'salary': '90,000'
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'location': 'Seattle, WA',
        'salary': '110,000'
    },
    {
        'id': 5,
        'title': 'Product Manager',
        'location': 'Boston, MA',
        'salary': '130,000'
    }
]


@app.route('/')
def hello_world():
    return render_template('index.html', jobs = JOBS, company_name = "Nishant Technologies")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)
