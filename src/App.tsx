import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import SymptomChecker from './pages/SymptomChecker';
import HealthEducation from './pages/HealthEducation';
import EmergencyGuide from './pages/EmergencyGuide';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/symptom-checker" element={<SymptomChecker />} />
            <Route path="/health-education" element={<HealthEducation />} />
            <Route path="/emergency-guide" element={<EmergencyGuide />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;