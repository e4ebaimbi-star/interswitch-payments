const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;
// Serve all files in web/ as static assets
app.use(express.static(path.join(__dirname, 'web')));
// Any unknown route returns index.html
const fetch = require('node-fetch');
// Proxy /api/status to the payment API container
// In Docker Compose, 'api' resolves to the payment-api container's IP
const API_URL = process.env.API_URL || 'http://localhost:4000';
app.get('/api/status', async (req, res) => {
    try {
        const response = await fetch(`${API_URL}/status`);
        const data = await response.json();
        res.json(data);
    } catch (err) {
        res.status(502).json({
            error: 'Payment API unavailable', detail:
                err.message
        });

    }
});
app.get('/api/health', async (req, res) => {
    try {
        const response = await fetch(`${API_URL}/health`);
        const data = await response.json();
        res.json(data);
    } catch (err) {
        res.status(502).json({ error: 'Payment API unavailable' });
    }
});
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'web', 'index.html'));
});
app.listen(PORT, () => {
    console.log(`Interswitch Portal running on port ${PORT}`);
    console.log(`Open: http://localhost:${PORT}`);
});