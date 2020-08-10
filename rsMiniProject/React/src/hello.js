/*class Person{
  constructor(name,age){
    this.name=name;
    this.age=age;
  }
}

const author =new Person(Rahul, 22)
*/
function Status(props){
  return (
    <h1> you are {props.status}. </h1>
  );
}
const element=<Status status="offline"/>;


function ShowName(props){
  return(
  <h2>{props.name}</h2>
  );
}

function ShowAge(props){
  return(
  <h2>{props.age}</h2>
  );
}

function ShowInfo(props){
  return (
    <div class="UserInfo">
      <ShowName name={props} />
      <ShowAge age={props} />
    </div>
  );
}


ReactDOM.render(
  element,
  document.getElementById('root')
);

class Clock extends React.Component {
  constructor(props){
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount(){
    this.timeID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount(){
    clearInterval(this.timerID);
  }

  tick(){
    this.setState({
      date: new Date()
    });
  }

  render(){
    return (
      <div>
        <h2> {this.state.date.toLocaleTimeString()} </h2>
      </div>
    );
  }
}

class Counter extends React.Component {
  constructor(props){
    super(props);
    this.state ={count: 0}
  }
  componentDidMount(){
    this.timeID = setInterval(
      () => this.addCount(),1000
    );
  }
  componentWillUnmount(){
    clearInterval(this.timeID);
  }
  addCount(){
    this.setState(
      {
        count: this.state.count+1
      }
    );
  }
  render(){
    return(
      <div>
        <h2>{this.state.count}</h2>
      </div>
    );
  }
}

class Toggle extends React.Component{
  constructor(props){
    super(props);
    this.state={toggleState: true};
    this.Change_state=this.Change_state.bind(this);
  }
  Change_state(){
    this.setState(state =>({
        toggleState:!(this.state.toggleState)
      })
    );
  }
  render(){
    return(
      <div>
        <button onClick={this.Change_state}>
          {this.state.toggleState ? 'ON':'OFF'}
        </button>
      </div>
    );
  }
}
ReactDOM.render(
  <Toggle />,
  document.getElementById('time')
);
