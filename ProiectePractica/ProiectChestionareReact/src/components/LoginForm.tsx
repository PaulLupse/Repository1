import React from 'react';

interface LoginFormProps {
    type:string
    loginCallback:(username:string, password:string)=>void
}

export function LoginForm(props: LoginFormProps) {

    const usernameInputRef = React.useRef<HTMLInputElement>(null);
    const passwordInputRef = React.useRef<HTMLInputElement>(null);

    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            justifyItems: 'center',
            marginTop: '10px',
            marginBottom: '10px',
            flexGrow: '1',
            maxWidth: '300px'
        }}>
            <div style={{marginRight: 'auto', marginLeft: 'auto'}}>
                <h2>{props.type}</h2>
            </div>
            <input ref={usernameInputRef} style={{marginBottom: '5px'}} placeholder='Username'/>
            <input ref={passwordInputRef} style={{marginBottom: '5px'}} placeholder='Password' type='password'/>
            <div style={{marginRight: 'auto', marginLeft: 'auto'}}>
                <button
                    onClick={
                        () => {
                            const usernameInput: HTMLInputElement | null = usernameInputRef.current
                            const passwordInput: HTMLInputElement | null = passwordInputRef.current

                            if (usernameInput && passwordInput && props.loginCallback) {
                                console.log(props.loginCallback);
                                props.loginCallback(usernameInput.value, passwordInput.value);

                            }
                        }
                    }

                >{props.type}
                </button>
            </div>
        </div>
    );
}