import logo from './logo.svg';
import './App.css';
import React from "react";


// get content from localhost:3000/about

class App extends React.Component {
  // Constructor 
  constructor(props) {
    super(props);

    this.state = {
      items: [],
      DataisLoaded: false
    };
  }
  

  loadData() {
    fetch(
      "http://localhost:3000/")
      .then((res) => res.text())
      .then((text) => {
        this.setState({
          items: text,
          DataisLoaded: true
        });
      })
  }

  componentDidMount() {
    this.loadData();
    // call loadData() function every 1s
    setInterval(() => {
      this.loadData();
    }
      , 1000);
  }

  render() {
    const { DataisLoaded, items } = this.state;

    if (!DataisLoaded) return <div>
      <h1> Loading.... </h1> </div>;

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            <div id="text">{items}</div>
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
