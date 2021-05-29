import logo from './logo.svg';
import './App.css';
import React, {Component} from "react";

class App extends Component {
    state = {levels: []}


    componentDidMount() {
        fetch("http://localhost:8000/level/all")
            .then((res) => res.json())
            .then((levels) => {
                console.log(JSON.stringify(levels, null, 2) +" "+levels[0].name);
                this.setState({levels});
                console.log(this.state);
            });
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <table>{ this.state.levels.map(level => <tr><td>{level.ulid}</td><td>{level.name}</td><td>{level.description}</td><td>{level.upload_date}</td><td><a href={"http://localhost:8000/level/download/?ulid="+level.ulid}>Download</a> </td></tr>)}</table>
                </header>
               </div>);

    }
}
export default App;
