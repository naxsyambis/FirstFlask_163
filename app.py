from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page and form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()  # Mengambil nama dari form
        age = request.form.get('age', '').strip()  # Mengambil umur dari form
        
        if name and age:  # Pastikan nama dan umur tidak kosong
            try:
                age = int(age)  # Mengonversi umur ke integer
                message = f"Selamat Ulang Tahun, {name}! Selamat merayakan ulang tahun ke-{age}!"  # Ucapan selamat ulang tahun
            except ValueError:  # Menangani jika input umur tidak valid
                message = f"Halo, {name}! Mohon masukkan umur yang valid."
        else:
            message = "Mohon isi nama dan umur dengan benar."
    
    return render_template('index.html', message=message)  # Kirim pesan ke template

if __name__ == '__main__':
    app.run(debug=True)