import config from '../config.json'

const url:string = config.baseURL;

export class LoginInfo {
    private _username;
    private _password;

    constructor(username:string, password:string) {
        this._username = username;
        this._password = password;

        Object.seal(this);
        Object.preventExtensions(this);
    }

    public get username() { return this._username; }
    public get password() { return this._password; }
}

export async function getAccessToken(loginInfo:LoginInfo) {

    const loginForm = new FormData();
    loginForm.append("username", loginInfo.username)
    loginForm.append("password", loginInfo.password)

    return await fetch(url+"/users/token", {method:"POST", body:loginForm});
}

// functie pt login in urma introducerii credentialelor
export async function login(username:string, password:string){

    // initial citim datele introduse in formular
    const loginInfo:LoginInfo = new LoginInfo(username, password);

    if(loginInfo === null)
        return undefined;

    try {

        const tokenResponse:Response = await getAccessToken(new LoginInfo(loginInfo.username, loginInfo.password));

        if(tokenResponse.ok) {

            console.log(`Logged in as ${loginInfo.username}.`);
            alert(`Logged in succesfuly as ${loginInfo.username}. Returning to main page.`);
            window.location.replace(url);
        }
        else {
            const errorMsg = "Server responded with status: " + tokenResponse.status + ".\nReturned message: " + (await tokenResponse.json()).message;
            throw new Error(errorMsg);
        }
    }
    catch(error) {
        alert(error);
    }
}

export async function register(username:string, password:string) {

    try {

        const requestHeader = new Headers({
            'Accept': "application/json",
            'Content-Type': "application/json"
        });

        const request = new Request(url + "/users/register", {
            method: "PUT",
            headers: requestHeader,
            body: JSON.stringify({
                username: username,
                password: password,
                email: (username != undefined) ? password : undefined
            })
        });

        const response = await fetch(request);
        if (response.ok) {
            const data = await response.json();
            alert(data.message);
        } else {
            const data = await response.json();
            throw new Error("Server has responded with status: " + response.status
                + ".\nReturned message: " + data.message);
        }
    } catch (error: any) {
        alert(error.toString());
    }
}

// functie pt login la accesarea paginii, returneaza numele utilizatorului curent
export async function auto_login() :Promise<string|undefined>{

    const loginRequest = new Request(
        url + "/users/me",
        {
            method:"POST",
            credentials:'include'
        })

    try {
        const loginResponse = await fetch(loginRequest);

        if(loginResponse.ok)
            return await loginResponse.json();
        else {
            const errorMsg:string = "Could not login. Please login manually.";
            throw new Error(errorMsg);
        }
    }
    catch(error) {
        return undefined;
    }
}

