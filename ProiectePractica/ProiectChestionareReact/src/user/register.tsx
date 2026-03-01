import React from 'react'
import {createRoot} from "react-dom/client";
import {LoginForm} from "../components/LoginForm";

function RegisterPage() {

    return (
        <div style={{height:'100vh', display:"flex", flexDirection:'column', alignItems:'stretch', justifyContent:'center'}}>
            <div style={{justifyContent:'center', display:'flex'}}>
                <LoginForm
                    type="Register"
                    loginCallback={
                        async()=>{
                            console.log('Registering...');
                        }
                    }
                />
            </div>
        </div>
    );
}

window.onload = ()=>{
    const rootDiv:HTMLDivElement = document.getElementById('root') as HTMLDivElement;
    const root = createRoot(rootDiv);
    root.render(<RegisterPage />);
}