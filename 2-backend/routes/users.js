const express = require('express');
const router  = express.Router();
const User    = require('../models/User');

router.post('/', async (req, res) => {
  try {
    const { fullName, email, password } = req.body;
    if (!fullName || !email || !password) return res.status(400).json({ success: false, message: 'fullName, email, and password are required' });
    const existing = await User.findOne({ email: email.toLowerCase() });
    if (existing) return res.status(409).json({ success: false, message: 'Email already exists' });
    const user = await User.create({ fullName, email, password });
    return res.status(201).json({ success: true, message: 'User created successfully', data: { id: user._id, fullName: user.fullName, email: user.email, createdAt: user.createdAt } });
  } catch (err) {
    if (err.name === 'ValidationError') return res.status(400).json({ success: false, message: err.message });
    return res.status(500).json({ success: false, message: 'Server error', error: err.message });
  }
});

router.get('/', async (req, res) => {
  try {
    const users = await User.find().select('-password');
    return res.status(200).json({ success: true, count: users.length, data: users });
  } catch (err) { return res.status(500).json({ success: false, message: 'Server error', error: err.message }); }
});

router.get('/:id', async (req, res) => {
  try {
    const user = await User.findById(req.params.id).select('-password');
    if (!user) return res.status(404).json({ success: false, message: 'User not found' });
    return res.status(200).json({ success: true, data: user });
  } catch (err) {
    if (err.name === 'CastError') return res.status(400).json({ success: false, message: 'Invalid user ID format' });
    return res.status(500).json({ success: false, message: 'Server error', error: err.message });
  }
});

router.delete('/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);
    if (!user) return res.status(404).json({ success: false, message: 'User not found' });
    return res.status(200).json({ success: true, message: `User "${user.fullName}" deleted successfully` });
  } catch (err) {
    if (err.name === 'CastError') return res.status(400).json({ success: false, message: 'Invalid user ID format' });
    return res.status(500).json({ success: false, message: 'Server error', error: err.message });
  }
});

module.exports = router;
