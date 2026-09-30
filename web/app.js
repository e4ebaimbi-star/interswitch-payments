// Live clock — updates every second
function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2, '0');
    const m = String(now.getMinutes()).padStart(2, '0');
    const s = String(now.getSeconds()).padStart(2, '0');
    document.getElementById('clock').textContent = `${h}:${m}:${s}`;
}
setInterval(updateClock, 1000);
updateClock();
// Animated stat counters
function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'));
    const step = target / (2000 / 16);
    let current = 0;
    const timer = setInterval(() => {
        current += step;
        if (current >= target) { current = target; clearInterval(timer); }
        el.textContent = Math.floor(current).toLocaleString();
    }, 16);
}
document.querySelectorAll('.counter').forEach(animateCounter);
// System status grid
const services = [
    { name: 'Payment API', status: 'operational' },
    { name: 'Verve Network', status: 'operational' },
    { name: 'Merchant Portal', status: 'operational' },
    { name: 'Settlement Engine', status: 'operational' },
    { name: 'Fraud Detection', status: 'operational' },
    { name: 'Notification Service', status: 'maintenance' },
];
const grid = document.getElementById('statusGrid');
services.forEach(s => {
    const card = document.createElement('div');
    card.className = `status-card ${s.status}`;
    card.innerHTML = `<span class="service-name">${s.name}</span>
<span class="service-status">${s.status === 'operational' ? '✔Operational' : '⚠ Maintenance'}</span>`;
    grid.appendChild(card);
});
// Form validation
function submitForm() {
    const name = document.getElementById('businessName').value.trim();
    const rc = document.getElementById('rcNumber').value.trim();
    const email = document.getElementById('email').value.trim();
    const type = document.getElementById('businessType').value;
    const msg = document.getElementById('formMessage');
    if (!name || !rc || !email || !type) {
        msg.className = 'form-message error';
        msg.textContent = 'Please fill in all fields before submitting.';
        return;

    }
    if (!email.includes('@') || !email.includes('.')) {
        msg.className = 'form-message error';
        msg.textContent = 'Please enter a valid email address.';
        return;
    }
    msg.className = 'form-message success';
    msg.textContent = `Application received for ${name}. We will contact
${email} within 2 business days.`;
}