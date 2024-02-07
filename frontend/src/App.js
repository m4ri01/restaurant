import {
  BrowserRouter as Router,
  Routes,
  Route,Navigate
} from "react-router-dom";
import { DailyHistory } from "./scene/DailyHistory";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/daily-history" />} />
        <Route path="/daily-history" element={<DailyHistory />} />
      </Routes>
    </Router>
  );
}

export default App;
