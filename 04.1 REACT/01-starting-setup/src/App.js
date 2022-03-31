import REACT from "react";
import Expenses from "./Components/Expenses/Expenses";
import NewExpense from "./Components/NewExpense/NewExpense";

function App() {
  return (
    <div>
      <NewExpense></NewExpense>
      <Expenses></Expenses>
    </div>
  );
}

export default App;
