
const baseURL = "http://175.24.4.124:5000";


export async function SignIn(formData) {
  try {
    let targetURL = `${baseURL}/signin`;
    let resp = await( fetch(targetURL, {
      method: "POST",
      mode: "cors",
      body: formData,
    }) );
    let json = await( resp.json() );
    console.log(`return json = ${ JSON.stringify(json) }`);

    return new Promise((resolve, reject) => {
      resolve(json);
    });
  }
  catch(error) {
    return new Promise((resolve, reject) => {
      reject("signin api failed");
    });
  }
}


export async function SignUp(formData) {
  let targetURL = `${baseURL}/signup`;
  let resp = await( fetch(targetURL, {
    method: "POST",
    mode: "cors",
    body: formData,
  }) );
  let json = await( resp.json() );
  console.log(`signup return json = ${ JSON.stringify(json) }`);

  return new Promise((resolve, reject) => {
    resolve(json);
  });
}


export async function getStudentInfo(studentID) {
  try {
    let targetURL = `${baseURL}/getStudentInfo/${studentID}`;
    // let targetURL = `${baseURL}/getStudentInfo`;
    console.log(`targetURL = ${targetURL}`);
    let resp = await( fetch(targetURL, {
      method: "GET",
      mode: "cors",
    }) );
    let json = await( resp.json() );

    console.log(`studentInfo, return JSON = ${JSON.stringify(json)}`);

    return new Promise((resolve, reject) => {
      resolve(json);
    });
  }
  catch(error) {
    throw new Error(error);
  }
}


export async function getTermList() {
  const targetURL = `${baseURL}/getTermInfo`;
  let resp = await( fetch(targetURL, {
    method: "GET",
    mode: "cors",
  }) );
  let text = await( resp.text() );
  let array = eval( text );     // 数组字符串转成JS数组
  console.log(`array = ${array} with type = ${Object.prototype.toString.call(array)}`);
  
  return new Promise((resolve, reject) => {
    resolve(array);
  })
}


export async function SearchCourse(formData) {
  const targetURL = `${baseURL}/searchCourse`;
  let resp = await(fetch(targetURL, {
    method: "POST",
    mode: "cors",
    body: formData,
  }));
  let json = await( resp.json() );
  console.log(`searchCourse: return json = ${ JSON.stringify(json) }`);

  return new Promise((resolve, reject) => {
    resolve(json);
  });
}