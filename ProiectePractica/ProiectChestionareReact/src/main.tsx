import React, {use} from 'react'
import {createRoot} from "react-dom/client";

interface DataProps {
    username:string
}

function DataDisplay(props:DataProps) {

    if(props.username === '') {
        return (
            <div style={{display:'flex', flexDirection:'column', alignItems:'center'}}>
                <h3>
                    You are not logged in.
                </h3>
                <a href="">Login</a>
                <a href="">Register</a>
            </div>
        )
    }
}

function Main() {

    const username:string = '';

    return (
        <div style={{display:"flex", flexDirection:"column", height:'100vh', minWidth:'300px', alignItems:'stretch'}}>

            <div style={{display:'flex'}}>
                <div style={{display:"flex", alignItems:'center', justifyContent:'center', maxWidth:'200px', flexGrow:'1'}}>
                    <p style={{textAlign:'center'}}>
                        Current user: {username?username:'none'}
                    </p>
                </div>
                <div style={{flexGrow:'1'}}>
                    <h1 style={{textAlign:'center'}}>
                        Main page
                    </h1>
                </div>
                <div style={{display:"flex", alignItems:'center', justifyContent:'center', maxWidth:'200px', flexGrow:'1'}}></div>
            </div>

            <div style={{display:'flex', flexDirection:'column', flexGrow:'1', maxWidth:'600px', marginLeft:'auto', marginRight:'auto', justifyContent:'center'}}>
                <DataDisplay username={username} />
            </div>

        </div>
    );
}

window.onload = ()=>{
    const rootDiv:HTMLDivElement = document.getElementById("root") as HTMLDivElement
    const root = createRoot(rootDiv);
    root.render(<Main />);
}