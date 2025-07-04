
```markdown
# 🚀 KD's Portfolio – Dockerized Flask App on AWS

This is a simple and elegant one-page **portfolio website** built using **Flask** (Python), styled with **HTML/CSS**, containerized using **Docker**, and deployed on an **AWS EC2** instance.

---

![Screenshot 2025-07-04 135346]


---

## 🛠️ Tech Stack

- **Backend**: Python 3.10, Flask
- **Containerization**: Docker, Docker CLI
- **Cloud Hosting**: AWS EC2 (Ubuntu 22.04)
- **DevOps Tools**: Docker Hub, Linux Terminal, Git & GitHub
- **UI**: HTML, CSS (Flexbox), Responsive Design

---

## ✨ Features

- 📄 One-page responsive portfolio layout
- 🐳 Fully Dockerized using a lightweight `Dockerfile`
- ☁️ Deployed on AWS EC2 with open security rules
- 📤 Published image to Docker Hub for portability

- 🔧 Resolved real-world deployment issues:
  - Docker permission denied (docker.sock)
  - AWS EC2 port/firewall issues
  - HTTPS/HTTP browser mismatch
  - Docker tagging and push authorization

---

## 🐳 Docker Usage

### 🔧 Build Image

```bash
docker build -t kd-portfolio .
````

### 🚀 Run Container

```bash
docker run -d -p 5000:5000 --name portfolio kd-portfolio
```



## ☁️ AWS EC2 Deployment Notes

To deploy this container on AWS EC2:

1. Launch an EC2 Ubuntu instance
2. Install Docker (`sudo apt install docker.io`)
3. Open port 5000 in your **security group**
4. Pull or build your Docker image
5. Run the container using `docker run -p 5000:5000 ...`

✅ Done — your app is live!

---

## 📤 Docker Hub Image

Pull it from Docker Hub:

```bash
docker pull kundan1729/portfolio:latest
```

View: [Docker Hub – kd23/portfolio](https://hub.docker.com/repository/docker/kd23/portfolio/tags)

---

## 🔗 Live Demo

🖥️ http\://<your-ec2-public-ip>:5000

> Replace with your actual IP or domain if mapped

---

## 📫 Contact

* 📧 Email: [kundan234432@gmail.com](mailto:kundan234432@gmail.com)
* 🔗 LinkedIn: [linkedin.com/in/kundan1729](https://linkedin.com/in/kundan1729)

---

## 📃 License

MIT License – free to use, modify, and distribute.

---

## 🙌 Acknowledgements

Inspired by the need for real-world DevOps practice.
If you found this helpful or want to collaborate, feel free to connect!

````

