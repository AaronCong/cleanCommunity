    var loginForm = document.querySelector('#login-form')
    var registerForm = document.querySelector('#register-form');
    var registerFormDumper = document.querySelector('#register-form-dumper')
    var itemNav = document.querySelector('#item-nav');
    var itemList = document.querySelector('#item-list');
    var avatar = document.querySelector('#avatar');
    var welcomeMsg = document.querySelector('#welcome-msg');
    var logoutBtn = document.querySelector('#logout-link');
    var itemNavDumper = document.querySelector('#item-nav-dumper');
    var isDumper = false;
    validateSession();
        
    function init() { 
        document.querySelector('#register-form-btn').addEventListener('click', showRegister);
        document.querySelector('#login-btn').addEventListener('click', login);
        document.querySelector('#register-btn').addEventListener('click', register);
        document.querySelector('#register-btn-dumper').addEventListener('click', register);

        //document.querySelector('#dumper').addEventListener('click', showRegisterFormDumper);
        document.querySelector('#non-dumper').addEventListener('click', showRegisterForm);
        document.querySelector('#login-form-btn').addEventListener('click', onSessionInvalid);
        document.querySelector('#login-form-btn-dumper').addEventListener('click', onSessionInvalid);
        //document.querySelector('#nearby-btn').addEventListener('click', loadNearbyHelpers);
    }


    function showElement(element, style) {
        var displayStyle = style ? style : 'block';
        element.style.display = displayStyle;
      }
    function validateSession() {
        onSessionInvalid();
        // The request parameters
        /*var url = './login';
        var req = JSON.stringify({});
    
        // display loading message
        //showLoadingMessage('Validating session...');
    
        // make AJAX call
        ajax('GET', url, req,
          // session is still valid
          function(res) {
            var result = JSON.parse(res);
    
            if (result.status === 'OK') {
              onSessionValid(result);
            }
          });*/
      }


      function login() {
        var username = document.querySelector("#username").value;
        var password = document.querySelector("#password").value;
        var url = "/login";
        var req = JSON.stringify({
            username: username,
            password: password
        });

        $.ajax({
            type: "post",
            url: url,
            data: {
                username: username,
                password: password
            },
            dataType: "json",
            success: [function (data) {
                // if (data === "success" ) {
                //     //onSessionValid();
                    var isDumper = document.querySelector("#is-dumper");
                    if(isDumper.checked == true) {
                      onSessionValidDumper();
                    } else {
                      onSessionValid();
                    }
                    // } else{
                    //     alert("用户名或者密码错误");
                    // }
            }],
                error : [function(data) {
                    alert("网络错误");
                }]
        });


       
      // error




      }
      
      function onSessionValid() {
        showElement(itemNav);
        hideElement(itemNavDumper);
        showElement(itemList);
        showElement(avatar);
        showElement(welcomeMsg);
        showElement(logoutBtn, 'inline-block');
        hideElement(loginForm);
        hideElement(registerForm);
        hideElement(registerFormDumper);
        loadNearbyHelpers();
      }

      function onSessionValidDumper() {
        showElement(itemNavDumper)
        hideElement(itemNav);
        showElement(itemList);
        showElement(avatar);
        showElement(welcomeMsg);
        showElement(logoutBtn, 'inline-block');
        hideElement(loginForm);
        hideElement(registerForm);
        hideElement(registerFormDumper);
        loadChatHistories();
      }


      function onSessionInvalid() {
        hideElement(itemNav);
        hideElement(itemNavDumper)
        hideElement(itemList);
        hideElement(avatar);
        hideElement(logoutBtn);
        hideElement(welcomeMsg);
        hideElement(registerForm);
        hideElement(registerFormDumper);
        //clearLoginError();
        showElement(loginForm);
      }
        function logout() {
            var url = "/logout";
            $.ajax({
            type: "post",
            url: url,
            data: {
                username: username,
                password: password,

            },
            dataType: "json",
            success: [function (data) {
                if (data === "success" ) {
                      alert('register successfully');
                    } else{
                        alert("register failed");
                    }
            }],
                error : [function(data) {
                    alert("网络错误");
                }]
        });
        }
      function register() {
        var url = "/register";
        var username = document.querySelector('#register-username').value;
        var password = document.querySelector('#register-password').value;
        var aptlat = parseFloat(document.querySelector('#apt-lat').value);
        var aptlon = parseFloat(document.querySelector('#apt-lon').value);

        if(isNaN(aptlat)) {
            //alert(aptlat);
            $.ajax({
            type: "post",
            url: url,
            data: {
                username: username,
                password: password,

            },
            dataType: "json",
            success: [function (data) {
                if (data === "success" ) {
                      alert('register successfully');
                    } else{
                        alert("register failed");
                    }
            }],
                error : [function(data) {
                    alert("网络错误");
                }]
        });
        } else {
            $.ajax({
            type: "post",
            url: url,
            data: {
                username: username,
                password: password,
                aptlat: aptlat,
                aptlon: aptlon
            },
            dataType: "json",
            success: [function (data) {
                if (data === "success" ) {
                      alert('register successfully');
                    } else{
                        alert("register failed");
                    }
            }],
                error : [function(data) {
                    alert("网络错误");
                }]
        });
        }

        
      }

    function loadNearbyHelpers() {
        var url = "/searchDumper";
        $.ajax({
            type: "get",
            url: url,
            dataType: "json",
            success: [function (data) {
                if(!data || data.length === 0) {
                    alert("No nearby helpers");
                } else {
                    //alert(data.length);
                    listHelpers(data);
                }
            }],
                error : [function() {
                    alert("网络错误");
                }]
        });
    }

    function loadChatHistories() {
        var url = "/listHistory";
        $.ajax({
            type: "get",
            url: url,
            dataType: "json",
            success: [function (data) {
                if(!data || data.length === 0) {
                    alert("No notifications");
                } else {
                    //alert(data.length);
                    listHistories(data);
                }
            }],
                error : [function() {
                    alert("网络错误");
                }]
        });
    }

    function listHistories(histories) {
        var historyList = document.querySelector('#item-list');
        historyList.innerHTML = '';
        for (var i = 0; i < histories.length; i++) {
            addItem2(historyList, histories[i]);
        }
    }

    function addItem2(helpers, helper) {
        //var helper_id = helper.helperID;
        var li = $create('li', {
            //id: 'item-' + helper_id,
            className: 'item'
        });
        li.appendChild($create('img', {
            src: helper.img
        }));
        var section = $create('div');
        var title = $create('a', {
            className: 'item-name'
        });
        title.innerHTML = helper.name;
        section.appendChild(title);
        var distance = $create('p', {
        className: 'item-distance'
        });
        distance.innerHTML = 'Message: ' + helper.uttr;
        section.appendChild(distance);

        var stars = $create('div', {
            className: 'stars'
        });

        for (var i = 0; i < 3; i++) {
        var star = $create('i', {
            className: 'fa fa-star'
        });
        stars.appendChild(star);
        }
        section.appendChild(stars);

        li.appendChild(section);
        helpers.appendChild(li);
    }

    function listHelpers(helpers) {
    var helperlist = document.querySelector('#item-list');
    helperlist.innerHTML = ''; // clear current results

    for (var i = 0; i < helpers.length; i++) {
      addItem(helperlist, helpers[i]);
    }
  }
    function addItem(helpers, helper) {
        var helper_id = helper.helperID;
        var li = $create('li', {
            id: 'item-' + helper_id,
            className: 'item'
        });
        li.appendChild($create('img', {
            src: helper.img
        }));
        var section = $create('div');
        var title = $create('a', {
            className: 'item-name'
        });
        title.innerHTML = helper.helperName;
        section.appendChild(title);
        var distance = $create('p', {
        className: 'item-distance'
        });
        distance.innerHTML = 'Distance: ' + helper.distance;
        section.appendChild(distance);

        var stars = $create('div', {
            className: 'stars'
        });

        for (var i = 0; i < 3; i++) {
        var star = $create('i', {
            className: 'fa fa-star'
        });
        stars.appendChild(star);
        }
        section.appendChild(stars);

        li.appendChild(section);
        helpers.appendChild(li);
    }

    function hideElement(element) {
        element.style.display ='none'
    }
    
    
    function showRegister() {
        var isDumper = document.querySelector('#is-dumper');
        if(isDumper.checked == true) {
            showRegisterFormDumper();
        } else {
            showRegisterForm();
        }
    }

    

    function showRegisterForm() {
        hideElement(itemNav);
        hideElement(itemNavDumper);
        hideElement(itemList);
        hideElement(avatar);
        hideElement(logoutBtn);
        hideElement(welcomeMsg);
        hideElement(loginForm);
        hideElement(registerFormDumper);
        //clearRegisterResult();
        showElement(registerForm);
      }  
      function showRegisterFormDumper() {
        hideElement(itemNav);
        hideElement(itemNavDumper);
        hideElement(itemList);
        hideElement(avatar);
        hideElement(logoutBtn);
        hideElement(welcomeMsg);
        hideElement(loginForm);
        hideElement(registerForm);
        //clearRegisterResult();
        showElement(registerFormDumper);
      }


      function $create(tag, options) {
        var element = document.createElement(tag);
        for (var key in options) {
          if (options.hasOwnProperty(key)) {
            element[key] = options[key];
          }
        }
        return element;
      }
    init();
