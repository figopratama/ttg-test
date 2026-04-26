require('dotenv').config();
const express  = require('express');
const mongoose = require('mongoose');
const app  = express();
const PORT = process.env.PORT || 3000;
app.use(express.json());
app.use('/api/users', require('./routes/users'));
app.get('/', (req, res) => res.json({ success: true, message: 'Tim Teknologi Global — User API', endpoints: { 'POST /api/users': 'Add new user', 'GET /api/users': 'Get all users', 'GET /api/users/:id': 'Get user by ID', 'DELETE /api/users/:id': 'Delete user by ID' } }));
app.use((req, res) => res.status(404).json({ success: false, message: `Route ${req.originalUrl} not found` }));
mongoose.connect(process.env.MONGO_URI)
  .then(() => { console.log('✅ MongoDB Atlas connected'); app.listen(PORT, () => console.log(`🚀 Server running on http://localhost:${PORT}`)); })
  .catch(err => { console.error('❌ MongoDB connection failed:', err.message); process.exit(1); });
