const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  fullName: { type: String, required: [true, 'Full name is required'], trim: true },
  email: { type: String, required: [true, 'Email is required'], unique: true, trim: true, lowercase: true, match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email'] },
  password: { type: String, required: [true, 'Password is required'], minlength: [8, 'Password must be at least 8 characters'] }
}, { timestamps: true });

module.exports = mongoose.model('User', userSchema);
