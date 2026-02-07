// Fetch projects from JSON file
async function fetchProjects() {
    try {
        const response = await fetch('projects.json'); // Fetch the JSON file
        const projects = await response.json(); // Convert to JS object
        renderProjects(projects); // Render projects on load
        updateProjectCounts(projects); // Update project counts
    } catch (error) {
        console.error("Error loading projects:", error);
    }
}

// Render projects dynamically based on filter
function renderProjects(projects, filter = 'all') {
    const projectsGrid = document.getElementById('projectsGrid');
    projectsGrid.innerHTML = '';

    const filteredProjects = filter === 'all' 
        ? projects 
        : projects.filter(project => project.category === filter);

    filteredProjects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.classList.add('project-card');
        
        const livePreviewLink = project.livePreview && project.livePreview !== "#" 
            ? `<a href="${project.livePreview}" class="project-link" target="_blank">
                <i class="fas fa-eye"></i> Live Preview
              </a>` 
            : '';

        const githubLink = project.githubLink && project.githubLink !== "#" 
            ? `<a href="${project.githubLink}" class="project-link" target="_blank">
                <i class="fab fa-github"></i> GitHub
              </a>` 
            : '';

        projectCard.innerHTML = `
            <h2 class="project-title">${project.title}</h2>
            <p class="project-description">${project.description}</p>
            <div class="tech-stack">
                ${project.techStack.map(tech => 
                    `<i class="tech-icon fas fa-${getTechIcon(tech)}"></i>`
                ).join('')}
            </div>
            <div class="hover-message">${project.hoverMessage}</div>
            <div class="project-links">
                ${livePreviewLink}
                ${githubLink}
            </div>
        `;
        projectsGrid.appendChild(projectCard);
    });
}

// Tech stack icon mapping
function getTechIcon(tech) { 
    const iconMap = {
        'Python': 'python',
        'TensorFlow': 'robot',
        'NLTK': 'brain',
        'Solidity': 'cubes',
        'React': 'react',
        'Web3.js': 'network-wired',
        'HTML': 'html5',
        'CSS': 'css3',
        'JavaScript': 'js',
        'Pandas': 'chart-bar',
        'Plotly': 'chart-line',
        'Bash': 'terminal',
        'Batch': 'window-maximize',
        'R': 'chart-pie',
        'Lua': 'moon'
    };
    return iconMap[tech] || 'code';
}

// Update project counts dynamically
function updateProjectCounts(projects) {
    const counts = {}; // Object to store category counts
    counts["all"] = projects.length; // Total projects

    // Count projects by category
    projects.forEach(project => {
        const categoryKey = project.category.replace(/\s+/g, "-"); // Convert spaces to dashes
        counts[categoryKey] = (counts[categoryKey] || 0) + 1;
    });

    // Update the UI with the counts
    Object.keys(counts).forEach(category => {
        const span = document.getElementById(`count-${category}`);
        if (span) {
            span.textContent = counts[category];
        }
    });
}

// Filter button functionality
document.getElementById('filterButtons').addEventListener('click', (e) => {
    if (e.target.classList.contains('filter-btn')) {
        const filterCategory = e.target.dataset.filter;

        // Remove active class from all buttons
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        
        // Add active class to clicked button
        e.target.classList.add('active');
        
        // Fetch projects and apply filter
        fetch('projects.json')
            .then(response => response.json())
            .then(projects => renderProjects(projects, filterCategory))
            .catch(error => console.error("Error loading projects:", error));
    }
});

// Daily coding tip generator
const codingTips = [
    "🌟 Pro Tip: Always write clean, readable code. Future you will thank you!",
    "💡 Remember: Good code is like a good joke. It needs no explanation.",
    "🚀 Learn one new programming concept every week. Consistency is key!",
    "🔍 Debugging is like being a detective in a crime movie where you're also the murderer.",
    "🌈 Embrace pair programming. Two brains are better than one!"
];

const funFacts = [
    "🚀 Python was named after Monty Python, not the snake! 🐍",
    "💡 The first computer bug was an actual moth found in a Harvard computer.",
    "🕹️ The first video game, 'Pong', was released in 1972!",
    "🌎 Over 70% of websites use JavaScript for interactivity."
];

function updateDailyTip() {
    const dailyTipElement = document.getElementById('dailyTip');
    const allMessages = [...codingTips, ...funFacts]; // Combine tips & fun facts
    const randomMessage = allMessages[Math.floor(Math.random() * allMessages.length)];
    dailyTipElement.textContent = randomMessage;
}

// Particle background effect
function createParticles() {
    const container = document.getElementById('particlesContainer');
    for (let i = 0; i < 100; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        particle.style.position = 'absolute';
        particle.style.width = `${Math.random() * 3}px`;
        particle.style.height = particle.style.width;
        particle.style.background = 'rgba(0, 255, 255, 0.5)';
        particle.style.borderRadius = '50%';
        particle.style.top = `${Math.random() * 100}%`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.animation = `float ${5 + Math.random() * 5}s infinite alternate`;
        
        // Animate movement
        setInterval(() => {
            particle.style.top = `${Math.random() * 100}%`;
            particle.style.left = `${Math.random() * 100}%`;
        }, 5000); // Moves every 5 seconds

        container.appendChild(particle);
    }
}

// 404 Easter Egg
function setupEasterEgg() {
    let secretCode = '';
    const revealCode = '404';

    document.addEventListener('keydown', (e) => {
        secretCode += e.key;
        
        if (secretCode.endsWith(revealCode)) {
            const easterEggDiv = document.createElement('div');
            easterEggDiv.style.position = 'fixed';
            easterEggDiv.style.top = '50%';
            easterEggDiv.style.left = '50%';
            easterEggDiv.style.transform = 'translate(-50%, -50%)';
            easterEggDiv.style.background = 'rgba(0, 0, 0, 0.9)';
            easterEggDiv.style.padding = '2rem';
            easterEggDiv.style.borderRadius = '15px';
            easterEggDiv.style.zIndex = '1000';
            easterEggDiv.innerHTML = `
                <h2 style="color: var(--neon-blue);">🚀 Hidden Developer Portal 🚀</h2>
                <p style="color: var(--text-primary);">Congratulations! You've unlocked the secret dev zone!</p>
            `;
            document.body.appendChild(easterEggDiv);

            // Remove after 3 seconds
            setTimeout(() => {
                document.body.removeChild(easterEggDiv);
            }, 3000);

            secretCode = ''; // Reset secret code
        }
    });
}

// Initialize page
async function init() {
    await fetchProjects();  // Load projects dynamically
    updateDailyTip();
    createParticles();
    setupEasterEgg();
}

// Run initialization
init();

// Add a fun console message
console.log(`
██████╗ ███████╗██╗   ██╗    ██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██║   ██║    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██║  ██║█████╗  ██║   ██║    ██████╔╝██║   ██║██████╔╝   ██║   
██║  ██║██╔══╝  ╚██╗ ██╔╝    ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██████╔╝███████╗ ╚████╔╝     ██║     ╚██████╔╝██║  ██║   ██║   
╚═════╝ ╚══════╝  ╚═══╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

Hey there, curious dev! 👋 
Peeking behind the curtain, eh? Keep exploring! 🕵️‍♀️🚀
`);