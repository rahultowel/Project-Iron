var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

/*class Person{
  constructor(name,age){
    this.name=name;
    this.age=age;
  }
}

const author =new Person(Rahul, 22)
*/
function Status(props) {
  return React.createElement(
    "h1",
    null,
    " you are ",
    props.status,
    ". "
  );
}
var element = React.createElement(Status, { status: "offline" });

function ShowName(props) {
  return React.createElement(
    "h2",
    null,
    props.name
  );
}

function ShowAge(props) {
  return React.createElement(
    "h2",
    null,
    props.age
  );
}

function ShowInfo(props) {
  return React.createElement(
    "div",
    { "class": "UserInfo" },
    React.createElement(ShowName, { name: props }),
    React.createElement(ShowAge, { age: props })
  );
}

ReactDOM.render(element, document.getElementById('root'));

var Clock = function (_React$Component) {
  _inherits(Clock, _React$Component);

  function Clock(props) {
    _classCallCheck(this, Clock);

    var _this = _possibleConstructorReturn(this, (Clock.__proto__ || Object.getPrototypeOf(Clock)).call(this, props));

    _this.state = { date: new Date() };
    return _this;
  }

  _createClass(Clock, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this2 = this;

      this.timeID = setInterval(function () {
        return _this2.tick();
      }, 1000);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      clearInterval(this.timerID);
    }
  }, {
    key: "tick",
    value: function tick() {
      this.setState({
        date: new Date()
      });
    }
  }, {
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "h2",
          null,
          " ",
          this.state.date.toLocaleTimeString(),
          " "
        )
      );
    }
  }]);

  return Clock;
}(React.Component);

var Counter = function (_React$Component2) {
  _inherits(Counter, _React$Component2);

  function Counter(props) {
    _classCallCheck(this, Counter);

    var _this3 = _possibleConstructorReturn(this, (Counter.__proto__ || Object.getPrototypeOf(Counter)).call(this, props));

    _this3.state = { count: 0 };
    return _this3;
  }

  _createClass(Counter, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this4 = this;

      this.timeID = setInterval(function () {
        return _this4.addCount();
      }, 1000);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      clearInterval(this.timeID);
    }
  }, {
    key: "addCount",
    value: function addCount() {
      this.setState({
        count: this.state.count + 1
      });
    }
  }, {
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "h2",
          null,
          this.state.count
        )
      );
    }
  }]);

  return Counter;
}(React.Component);

var Toggle = function (_React$Component3) {
  _inherits(Toggle, _React$Component3);

  function Toggle(props) {
    _classCallCheck(this, Toggle);

    var _this5 = _possibleConstructorReturn(this, (Toggle.__proto__ || Object.getPrototypeOf(Toggle)).call(this, props));

    _this5.state = { toggleState: true };
    _this5.Change_state = _this5.Change_state.bind(_this5);
    return _this5;
  }

  _createClass(Toggle, [{
    key: "Change_state",
    value: function Change_state() {
      var _this6 = this;

      this.setState(function (state) {
        return {
          toggleState: !_this6.state.toggleState
        };
      });
    }
  }, {
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "button",
          { onClick: this.Change_state },
          this.state.toggleState ? 'ON' : 'OFF'
        )
      );
    }
  }]);

  return Toggle;
}(React.Component);

ReactDOM.render(React.createElement(Toggle, null), document.getElementById('time'));