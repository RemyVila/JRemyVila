// base styling
import "./App.css";

// re-ro-do route handling imports
import { Switch, Route, useHistory } from "react-router-dom";

// component imports
import Landing from "./components/Landing/Landing";

function App() {
  return (
    <Switch>
      <Route exact path="/" component={Landing} />
    </Switch>
  );
}

export default App;
