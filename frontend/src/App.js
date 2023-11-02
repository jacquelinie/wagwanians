import geoff from './geoff.jpeg';
import './App.css';

function App() {
  document.title = "Wagwanians";
  return (
    // <>
    //   <Routes>
    //     <Route path=" 'Path' " element={< 'Name of Page' />} />
    //      ... add more routes
    //   </Routes>
    // </>
    <div className="App">
      <header className="App-header">
        <img src={geoff} className="App-logo" alt="logo" />
        <p>
          This is Geoffrey.
        </p>
      </header>
    </div>
  );
}

export default App;
