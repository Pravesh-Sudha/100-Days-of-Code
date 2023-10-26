# Day 50 of 100DaysofCode

Feeling excited to start Day 50 of 100 DaysOfCode, today, I created an AWS DevOps project. This project provides a beginner guide to AWS, its services like aws s3, artifact, codebuild, code commit, code deploy and many more. For referneces, [Watch](https://youtu.be/IUF-pfbYGvg?si=hu1DHRhcbn2rfT6W) the video.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-50
```

# Resume Website 

A resume website is an excellent way to showcase your skills, experience, and portfolio to potential employers or clients.

## Step 1: Create Your Project Directory

1. Create a new folder on your local computer to store your project files.
2. Inside the folder, create two new files: `index.html` and `style.css`. The `index.html` file will contain the content of your website, and the `style.css` file will define its appearance.

## Step 2: Write HTML Content

Open the `index.html` file in your code editor and write the HTML structure for your resume website. Here's a simple example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Your Name - Resume</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <header>
        <h1>Your Name</h1>
        <p>Web Developer</p>
    </header>
    
    <section id="about">
        <h2>About Me</h2>
        <p>Your introduction and brief bio here.</p>
    </section>
    
    <!-- Add more sections for experience, education, skills, and portfolio -->
    
    <footer>
        <p>Contact Information</p>
    </footer>
</body>
</html>
```

Replace "Your Name," the content, and the additional sections as needed.

## Step 3: Create CSS Styles

Open the `style.css` file and write the CSS code to style your website. Here's a basic example:

```css
/* Reset some default styles */
body, h1, p {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

header {
    text-align: center;
    background-color: #333;
    color: #fff;
    padding: 20px;
}

#about {
    background-color: #fff;
    padding: 20px;
}

/* Define more styles for other sections and elements */
```

Customize the styles to match your preferences and branding.

## Step 4: Test Locally

Open the `index.html` file in your web browser to preview your website locally. Make sure it looks and functions as expected.

## Step 5: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in with your account.
2. Click on the "+" sign in the top right corner and select "New repository."
3. Give your repository a name, and make it public or private (depending on your preferences).
4. Click "Create repository."

## Step 6: Push Your Code to GitHub

Follow the instructions provided by GitHub to push your local project to the GitHub repository you just created. This typically involves running a few Git commands in your command line:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```

Replace `<repository-url>` with the URL of your GitHub repository.

## Step 7: Set Up GitHub Pages

1. In your GitHub repository, navigate to the "Settings" tab.
2. Scroll down to the "GitHub Pages" section.
3. In the "Source" dropdown, select the branch you want to use for GitHub Pages (usually "main").
4. Click "Save."
