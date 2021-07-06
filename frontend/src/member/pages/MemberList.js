  
import React,{ useState } from 'react'
import '../styles/MemberLogin.css'
import { MemberListComponent2 } from 'member'
import { MemberMenu as Menu } from 'common'
import { MemberNav as Nav } from 'member'
const MemberList = () => {
return (<>
<Nav/>
    <table style={{width: '100%', height: '100%'}}>
        <tr>
            <td style={{width: '20%'}}> <Menu/> </td>
            <td style={{width: '80%'}}> <MemberListComponent2/> </td>
        </tr>
    </table>
</>)
}

export default MemberList;